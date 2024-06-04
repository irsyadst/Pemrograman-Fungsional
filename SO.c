/* #include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

#include <string.h>
#include <sys/wait.h>

int
main(int argc, char *argv[])
{
  printf("hello world (pid:%d)\n", (int) getpid());

  int rc = fork();
  if (rc < 0) {
    fprintf(stderr, "fork failed\n");
    exit(1);
  } else if (rc == 0) { // child (new process)
    printf("hello, I am child (pid: %d)\n", (int) getpid());
    char *myargs[3];
    myargs[0] = strdup("wc");
    myargs[1] = strdup("p3.c");
    myargs[2] = NULL;
    execvp(myargs[0], myargs);
    printf("this shouldn't print out");
  } else { // parent goes down this path (main)
    int wc;
    wait(&wc);
    printf("hello, I am parent of %d (wc:%d) (pid:%d)\n",
           rc, wc, (int) getpid());
  }
  return 0;
} */
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
  int i = 100;

  printf("Nilai dari i sebelum fork: %d\n", i);

  int rc = fork();
  if (rc < 0) {
    fprintf(stderr, "fork failed\n");
    exit(1);
  } else if (rc == 0) { // child (new process)
    printf("Nilai dari i di child: %d\n", i);
    i = 200;
    printf("Nilai dari i di child setelah diganti: %d\n", i);
  } else { // parent goes down this path (main)
    printf("Nilai dari i di parent: %d\n", i);
    i = 300;
    printf("Nilai dari i di parent setelah diganti: %d\n", i);
  }

  return 0;
}