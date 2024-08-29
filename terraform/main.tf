# main.tf

provider "aws" {
  region = "us-east-2"
}
# Backend configuration
terraform {
  backend "s3" {
    bucket = "tfstatelab"
    key    = "statefile/terraform.tfstate"  # Change the path as needed
    region = "us-east-2" 
  }
}

resource "aws_vpc" "main_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public_subnet_1" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-2a"  # Corrected zone
  map_public_ip_on_launch = true
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-2b"  # Corrected zone
  map_public_ip_on_launch = true
}