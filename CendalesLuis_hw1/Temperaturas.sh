wget https://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts.txt

awk 'NR>8{if($13>0 && !($1=="Year"))print $1}' GLB.Ts.txt > TempDic.txt

awk 'NR>8{if($1!="Year" && NF==20)print $1,$14/100}' GLB.Ts.txt > TempPomedios.txt

awk 'NR>8 && NR<140{if($1!="Year")print $7}' GLB.Ts.txt > TempJun.txt

python plotTemp.py

rm GLB.Ts.txt
