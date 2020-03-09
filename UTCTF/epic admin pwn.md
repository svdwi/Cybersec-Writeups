** **Write-up : epic admin pwn***

this challenge is epic i promise the flag is the password. 

> DESCRIPTION

First when u open the website there are login page so tried SQL Injection To check it . i use `' OR 1 = 1 -- -` its work but we don't get any flag just welcome message u_u so is injectable but no flag there cuz the flag is the password so i use  *sqlmap* to save time .

    sqlmap -u 'http://web2.utctf.live.5006/' --data="username=';SELECT * from user --&pass=" --risk=1 -D public -T users --dump

![enter image description here](https://lh3.googleusercontent.com/4COo739x7evAl1ymRkVrUlbmRLAyuy7Qn-S5YPoux7enKQw7EI7V32U4xJSlrmK9dGxe4QZ9PQas0mXB5MYwBxZ5XSCV5HwtFjIlYWXNk82FebXrOyr4jyFIPYjCnecukJyfGCwNzTUQUuhXvPD6_wOTPOQrMgt_eABbZPqpdCDiBaz6oAAOIAhWOf3FLhRmu4u0S3lEaqLd_eZritFq_6pXJNtCjKAnHYQO3FKFknaFlIsK5FxCt0_Pcpnbfozx91ktHdc-D3kz-ho7YeC1D0CzcThWkfiYbHJ-jWTtrA6RlHBODGY0Nr8Et5c1F2B4KEQXYVR07gxjC7iwGbxMm3WtubpnErNwxMGaB39adpjjtfHEoR93iU477ttaC4AYjhfTpwFFmwg5TEeD8mZNroXhiNPicrPliiYmWOtPLn_EcATi6XaNNsQ9PH3fzV6I4yCLvnBPKrJa_w_C00AdpdkjzQt7q3EJuOSPwov0eKe_555ccXDvOacW_lmeJhk0bsXK0hMUCvrGWyRfbDBNvKSKvvfGleXr1reHvguH5yDjYN--m7-hWA0lSlif4vu9iJIMv0og8QDWXEYML6eyOnsENXJT6YKto_j1KwTX4bKztSuHF1bUcfqWauD3KnxVXzXIdzowwSpCrRxD5QbCNgoUPuH5As23WGvgQvPYNlhIgSU3Usbu=w777-h374-no)
