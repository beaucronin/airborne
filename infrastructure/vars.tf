variable "aws_access_key" {}
variable "aws_secret_key" {}
variable "region" {
  description = "The region to apply these templates to (e.g. us-east-1)"
  default = "us-west-2"
}

variable "opensky_states_table" {
  description = "The DynamoDB table that contains OpenSky states"
  default = "OpenSky_States"
}
