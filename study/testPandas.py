import pandas
pdData={
    '股票代码':lists[0],
    '名称':lists[1],
    '现价':lists[2],
    '涨跌幅/%':lists[3],
    '涨跌':lists[4],
    '涨速/%':lists[5],
    '换手/%':lists[6],
    '量比':lists[7],
    '振幅/%':lists[8],
    '成交额':lists[9],
    '流通股':lists[10],
    '流通市值':lists[11],
    '市盈率':lists[12],
}
df = pandas.DataFrame(pdData)
df.to_csv('同花顺2.csv', index=False, encoding='utf-8')