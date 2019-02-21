#!/bin/zsh

echo ""
echo "================================"
echo "テーブル削除"
aws dynamodb delete-table --table-name accounts --endpoint-url http://localhost:8000
echo ""

echo ""
echo "================================"
echo "dynamodbのテーブル確認"
aws dynamodb list-tables --endpoint-url http://localhost:8000
echo ""

echo ""
echo "================================"
echo "dynamodbへcitiesのテーブル作成"
aws dynamodb create-table --table-name 'accounts' \
--attribute-definitions '[{"AttributeName":"key","AttributeType": "S"}]' \
--key-schema '[{"AttributeName":"key","KeyType": "HASH"}]' \
--provisioned-throughput '{"ReadCapacityUnits": 5,"WriteCapacityUnits": 5}' \
--endpoint-url http://localhost:8000
echo ""

echo ""
echo "================================"
echo "データ挿入"
aws dynamodb put-item --table-name cities --item '{ "population": { "N": "38164" }, "date_mod": { "S": "1950-6-22" }, "key": { "S": "t0924" }, "name": { "S": "足利" } }' --endpoint-url http://localhost:8000
aws dynamodb put-item --table-name cities --item '{ "population": { "N": "72391" }, "date_mod": { "S": "1950-8-30" }, "key": { "S": "t0925" }, "name": { "S": "日光" } }' --endpoint-url http://localhost:8000
aws dynamodb put-item --table-name cities --item '{ "population": { "N": "56148" }, "date_mod": { "S": "1950-9-7" }, "key": { "S": "t0926" }, "name": { "S": "下野" } }' --endpoint-url http://localhost:8000
echo ""

echo ""
echo "================================"
echo "dynamodbのテーブル確認"
aws dynamodb list-tables --endpoint-url http://localhost:8000
echo ""

