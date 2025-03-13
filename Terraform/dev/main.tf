terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.0"
        }
    }
    backend "local" {
      path = "terraform.tfstate"
    }
}

provider "aws" {
    region = "eu-west-2"
}

module "dynamodb" {
    source = "../modules/dynamodb"
    table_name = "PersonConversionHistory"
}