import boto3
from django.db.models.expressions import Expression
from book_store.Services.dbfile import database_details


def get_dbDetails(client):

    return database_details[client]

def dynamodbPutItem(client,table_name,data):
    try:
       client_details = get_dbDetails(client)

       dynamodb = boto3.resource('dynamodb',
                                  endpoint_url=client_details["endpoint_url"],
                                  region_name=client_details["region_name"],
                                  aws_access_key_id=client_details["aws_access_key_id"],
                                  aws_secret_access_key=client_details["aws_secret_access_key"])    
       table = dynamodb.Table(table_name)

       table.put_item(
                        Item = data
                    )

       return True
    except Exception as err:
        return err
    
def dynamodbGetItem(client,table_name,key_name):

    try:
        client_details = get_dbDetails(client)

        dynamodb = boto3.resource('dynamodb',
                                    endpoint_url=client_details["endpoint_url"],
                                    region_name=client_details["region_name"],
                                    aws_access_key_id=client_details["aws_access_key_id"],
                                    aws_secret_access_key=client_details["aws_secret_access_key"])    
        table = dynamodb.Table(table_name)

        try:
            response = table.get_item(Key=key_name)
            return response['Item']

        except Exception as e:
            print(e.response['Error']['Message'])

    except Exception as err:
        print("query error",err)
        return err

def dynamodbUpdateItem(client,table_name,key_name,updated_values):
    try:
        client_details = get_dbDetails(client)

        dynamodb = boto3.resource('dynamodb',
                                    endpoint_url=client_details["endpoint_url"],
                                    region_name=client_details["region_name"],
                                    aws_access_key_id=client_details["aws_access_key_id"],
                                    aws_secret_access_key=client_details["aws_secret_access_key"])    
        table = dynamodb.Table(table_name)
        updateExpression="set "
        ExpressionAttributeValues={}
        keys_data = list(updated_values.keys())
       

        for i in range(0,len(keys_data)):
            if i < len(keys_data)-1:
                updateExpression+= keys_data[i]+"=:"+keys_data[i]+","
                ExpressionAttributeValues[":"+keys_data[i]] = updated_values[keys_data[i]]
            else:
                updateExpression+= keys_data[i]+"=:"+keys_data[i]
                ExpressionAttributeValues[":"+keys_data[i]] = updated_values[keys_data[i]]
       
        try:

            table.update_item(
                Key=key_name,
                UpdateExpression=updateExpression,
                ExpressionAttributeValues=ExpressionAttributeValues
            )

        except Exception as error:
            print("update error",error)
        # print("query done")
        # print("result of update item",res)

        # print("update Expression",updateExpression)
        # print("Expression Attribute values",ExpressionAttributeValues)
        return True

    except Exception as err:
        return err

def dynamodbDeleteItem(client,table_name,key_name):
    try:
        print(0)
    except print(0):
        pass