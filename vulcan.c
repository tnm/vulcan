#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <time.h>
#include <limits.h>
#include <pthread.h>
#include "hiredis/hiredis.h"

#define NUM_THREADS 40
#define COMMAND_LEN 10

#define STRING 1
#define LIST 2
#define SET 3
#define ZSET 4

// defaults
char *hostname = "127.0.0.1";
int port = 6390;

void usage() {
    printf("usage: ./vulcan [number of keys] [string|list|set|zset] -h [host] -p [port] \n");
    exit(1);
}

struct vulcan_params {
    int unique_id;
    long count;
    int type;
    char command[COMMAND_LEN];
} typedef vulcan_params_t;

void generate_data(void *vulcan_params_pt) {
    vulcan_params_t *vulcan_params = (vulcan_params_t*) vulcan_params_pt;

    int id     = vulcan_params->unique_id;
    long count = vulcan_params->count;
    int type   = vulcan_params->type;

    char command[COMMAND_LEN];
    strcpy(command, vulcan_params->command);

    // get a Redis context and connection
    redisContext *context;
    struct timeval timeout = { 3, 500000 }; // 3.5 seconds
    context = redisConnectWithTimeout(hostname, port, timeout);
    if (context == NULL || context->err) {
        if (context) {
            fprintf(stderr, "[vulcan] Redis connection error: %s\n", context->errstr);
            redisFree(context);
        } else {
            fprintf(stderr, "[vulcan] Redis connection error: can't allocate redis context\n");
        }
        exit(1);
    }

    redisReply *reply;
    for (long i = 0; i < count; i++) {
        // build the string key, using the unique id and the iteration number
        char key[80];
        sprintf(key, "%i:%i:%ld", type, id, i);

        // set the key with a test value, special case for ZSET
        if (type == ZSET) {
            reply = redisCommand(context, "%s %s %s %i", command, key, "test", rand());
        } else {
            reply = redisCommand(context, "%s %s %s", command, key, "test");
        }

        freeReplyObject(reply);
    }

    redisFree(context);
    free(vulcan_params_pt);
    pthread_exit(NULL);
}

int main(int argc, char **argv) {
    if (argc < 3) usage();

    // Parse arguments
    long count = strtol(argv[1], NULL, 10);
    if (errno == ERANGE) {
        fprintf(stderr, "[vulcan] Requested count is greater than LONG_MAX, using %ld.\n", LONG_MAX);
    }

    char *type = argv[2];

    if (argc > 3) {
        if (strncmp(argv[3], "-h", 2) == 0) {
            if (argv[4] != NULL) {
                hostname = argv[4];
            } else {
                usage();
            }
        } else {
            usage();
        }

        if (argc > 5) {
            if (strncmp(argv[5], "-p", 2) == 0) {
                if (argv[6] != NULL) {
                    port = atoi(argv[6]);
                } else {
                    usage();
                }
            } else {
                usage();
            }
        }
    }

    fprintf(stderr, "[vulcan] Using hostname %s and port %i\n", hostname, port);

    // Determine type
    int data_type;
    char command[COMMAND_LEN];

    if (strncmp(type, "string", 6) == 0) {
        data_type = STRING;
        strcpy(command, "SET");
    } else if (strncmp(type, "list", 4) == 0) {
        data_type = LIST;
        strcpy(command, "LPUSH");
    } else if (strncmp(type, "set", 3) == 0) {
        data_type = SET;
        strcpy(command, "SADD");
    } else if (strncmp(type, "zset", 4) == 0) {
        data_type = ZSET;
        strcpy(command, "ZADD");
    } else {
        usage();
    }

    // Do the work and time it. We'll print timing data to stderr.
    struct timeval t1, t2;
    double elapsed_time;
    gettimeofday(&t1, NULL);

    // Each thread does 1/NUM_THREADS of the work
    pthread_t threads[NUM_THREADS];
    long per_thread = count / NUM_THREADS;

    long t;
    for (t = 0; t < NUM_THREADS; t++) {
        // build the vulcan_params struct
        vulcan_params_t *data = (vulcan_params_t*) malloc(sizeof(vulcan_params_t));
        if (data == NULL) {
            fprintf(stderr, "malloc failed");
            exit(-1);
        }

        data->unique_id = t;
        data->count = per_thread;
        data->type = data_type;
        strcpy(data->command, command);

        pthread_create(&threads[t], NULL, (void *) generate_data, (void *) data);
    }

    for (t = 0; t < NUM_THREADS; t++) {
        (void) pthread_join(threads[t], NULL);
    }

    gettimeofday(&t2, NULL);
    elapsed_time =  (t2.tv_sec - t1.tv_sec) * 1000.0;
    elapsed_time += (t2.tv_usec - t1.tv_usec) / 1000.0;
    fprintf(stderr, "[vulcan] set %ld %ss in %lf milliseconds\n", count, type, elapsed_time);

    return 0;
}
