#!/bin/zsh

echo ""
echo "================================"
echo "dynamodbのテーブル確認"
aws dynamodb list-tables --endpoint-url http://localhost:8000
echo ""

echo ""
echo "================================"
echo "初期化(テーブル削除)"
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
echo "dynamodbのテーブル確認"
aws dynamodb list-tables --endpoint-url http://localhost:8000
echo ""

echo ""
echo "================================"
echo "dynamodbのテーブル内容確認(テーブル作成直後)"
aws dynamodb describe-table --endpoint-url http://localhost:8000 \
--table-name accounts
echo ""

echo ""
echo "================================"
echo "データ挿入"
# TODO: ここはTypescriptで実装した方がいいかな
for i in {0..3}; do
  CNT=`echo "$i"`
  aws dynamodb put-item --table-name accounts --item '{ "no": { "N": "38164" }, "date_mod": { "S": "1950-6-22" }, "key": { "S": "1" }, "name": { "S": "足利" } }' --endpoint-url http://localhost:8000
done
echo ""

echo ""
echo "================================"
echo "dynamodbのテーブル内容確認(データ挿入直後)"
aws dynamodb describe-table --endpoint-url http://localhost:8000 \
--table-name accounts
echo ""

echo ""
echo "================================"
echo "テーブル内容の表示"
aws dynamodb scan --endpoint-url http://localhost:8000 \
--table-name accounts
echo ""


