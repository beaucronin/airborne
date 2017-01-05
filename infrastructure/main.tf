provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region = "${var.region}"
}

resource "aws_dynamodb_table" "opensky_states" {
	name = "${var.opensky_states_table}"
	read_capacity = 1
	write_capacity = 10
	hash_key = "icao24"
	attribute {
		name = "icao24"
		type = "S"
	}
}
