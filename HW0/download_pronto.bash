mkdir pronto

cd pronto
echo "Pronto bike data from 10/13/14 to 10/12/15" > README.txt

mkdir data
cd data
curl -O "https://s3.amazonaws.com/pronto-data/open_data_year_one.zip"

unzip "open_data_year_one.zip"

head "2015_trip_data.csv"
