resource "aws_dynamodb_table" "dynamodb" {
    name = var.table_name
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "person_id"
    range_key = "conversation_id"

    attribute {
        name = "person_id"
        type = "S"
    }

    attribute {
        name = "conversation_id"
        type = "S"
    }

    attribute {
        name = "timestamp"
        type = "N"
    }

    global_secondary_index {
        name = "Person_Timestamp_Index"
        hash_key = "person_id"
        range_key = "timestamp"
        projection_type = "ALL"
    }
}