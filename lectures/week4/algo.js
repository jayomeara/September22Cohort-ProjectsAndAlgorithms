// Given an array that could contain indexes of arrays,
// determine the amount of numbers in all indexes. Example:
// lengthNested( [4,[],8,[9,6,3],7] ) returns 6.
// Do not consider there being a third level of nesting
// (something such as [11,[[6]]]).


arrThree = [4,[],8,[9,6,3],7]
function lengthNested(arr) {
    let count = 0;
  
    for (i = 0; i < arr.length; i++) {
      if (Array.isArray(arr[i])) {
        for (let j = 0; j < arr[i].length; j++) {
          if (!Number.isNaN(arr[i][j])) {
            count++;
          }
        }
      } else {
        if (!Number.isNaN(arr[i])) {
          count++;
        }
      }
    }
  
    return count;
  }
  lengthNested([[6], 5, "hi", [], [undefined, 3], 2, 7]);



from server import app as application
if __name__ == "__main__":
    application.run()

server {
  listen 80;
  server_name 34.232.80.227;
  location / {
    include proxy_params;
    proxy_pass http://unix:/home/ubuntu/codingdojo_GroupLucky13/codingdojo_GroupLucky13.sock;
  }
}
sudo ln -s /etc/nginx/sites-available/codingdojo_GroupLucky13 /etc/nginx/sites-enabled

sudo vim /etc/nginx/sites-available/codingdojo_GroupLucky13

[Unit]
Description=Gunicorn instance
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/codingdojo_GroupLucky13
Environment="PATH=/home/ubuntu/codingdojo_GroupLucky13/venv/bin"
ExecStart=/home/ubuntu/codingdojo_GroupLucky13/venv/bin/gunicorn --workers 3 --bind unix:codingdojo_GroupLucky13.sock -m 007 wsgi:application
[Install]
WantedBy=multi-user.target

invoke-rc.d mysql start