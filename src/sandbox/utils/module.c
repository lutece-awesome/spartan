#include "module.h"
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>

bool is_privilege_user(){
    return geteuid() != 0;
}
