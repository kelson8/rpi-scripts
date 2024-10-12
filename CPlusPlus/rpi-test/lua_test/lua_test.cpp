#include <stdio.h>
#include <string.h>


// This doens't seem to work just yet.:
//... I installed it from the source package and added the include directories like this and it built?
// What changed..

extern "C"{
#include "include/lua/lua.h"
#include "include/lua/lualib.h"
#include "include/lua/lauxlib.h"
}

int main(void) {
    puts("lua interpretor:");
    char buff[256];
    int error;

    lua_State *L = luaL_newstate(); /* opens Lua */
    luaL_openlibs(L); /* opens the standard libraries */

    while (fgets(buff, sizeof(buff), stdin) != NULL) {
        error = luaL_loadbuffer(L, buff, strlen(buff), "line") ||
                lua_pcall(L, 0, 0, 0);
        if (error) {
            fprintf(stderr, "%s", lua_tostring(L, -1));
            lua_pop(L, 1); /* pop error message from the stack */
        }
    }
    lua_close(L);
    return 0;
}
