TD-IDF: データ取得プロセス

1. getWiki_category.py
httpでwikipediaに接続し, 対象カテゴリ傘下の記事タイトルを取得する.
for i in range(2): #数字で深さ指定
    call = page.reCall(main_list)
このコード部分にて傘下数を指定.
指定をしないとデータ数が大量になるため, 指定した.

プログラム実行により, カテゴリごとに記事タイトルが羅列したファイルが生成される.

2. duplicate_arrange.py
1で作成されたファイルにおいて, タイトルが重複しないよう再構成.

3. get_wikidata_*****.py
2で作成されたファイルを元に, タイトルの記事データを取得し, ファイルに書き込み

4. その他データ
ディレクトリ: sougou_Data
3のデータを格納

ディレクトリ: title
2のデータを格納
# 0929_getWikiData
# 0929_getWikiData
# 0929_getWikiData
