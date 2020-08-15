var client = new HttpClient();

function up() {
  var client = new HttpClient();
  client.get('http://192.168.1.88/api?command=1&speed=10&track=44', function(response) {});
  client.get('http://192.168.1.88/api?command=1&speed=10&track=45', function(response) {});
}

function down() {
  var client = new HttpClient();
  client.get('http://192.168.1.88/api?command=2&speed=10&track=44', function(response) {});
  client.get('http://192.168.1.88/api?command=2&speed=10&track=45', function(response) {});
}

function stop() {
  var client = new HttpClient();
  client.get('http://192.168.1.88/api?command=0&speed=10&track=44', function(response) {});
  client.get('http://192.168.1.88/api?command=0&speed=10&track=45', function(response) {});
}