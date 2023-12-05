# 0x0F. Load balancer
You have been given 2 additional servers:

    gc-[STUDENT_ID]-web-02-XXXXXXXXXX
    gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let's improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

TASK | DESCRIPTION
--- | ---
`0-custom_http_response_header` | Configure web-02 to be identical to web-01
`1-install_load_balancer` | Install and configure HAproxy on your lb-01 server to send traffice to web-01 and web-02
`2-puppet_custom_http_response_header.pp` | Puppet automation to configure web-02 to be identical to web-01
