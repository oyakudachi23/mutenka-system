import csv
from pathlib import Path

CSV_FILE = "products.csv"
OUTPUT_FILE = "index.html"


def score_product(product):
    price = int(product["price"])
    rating = float(product["rating"])
    review_count = int(product["review_count"])

    price_score = max(0, 100 - price / 30)
    rating_score = rating * 20
    review_score = min(review_count / 2, 100)

    return price_score * 0.4 + rating_score * 0.4 + review_score * 0.2


def load_products():
    with open(CSV_FILE, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        products = list(reader)

    products.sort(key=score_product, reverse=True)
    return products


def generate_html(products):
    rows = ""

    for i, p in enumerate(products, start=1):
        rows += f"""
        <tr>
            <td>{i}</td>
            <td><img src="{p['image']}" alt="{p['name']}"></td>
            <td>{p['name']}</td>
            <td>{p['shop']}</td>
            <td>{int(p['price']):,}円</td>
            <td>{p['rating']}</td>
            <td>{p['review_count']}件</td>
            <td><a class="button" href="{p['url']}" target="_blank" rel="nofollow sponsored noopener">詳細を見る</a></td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>無添加ベーコンおすすめ比較</title>
    <meta name="description" content="無添加ベーコンを価格・口コミ・レビュー件数で比較します。">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: sans-serif;
            line-height: 1.8;
            margin: 0;
            background: #fafafa;
            color: #333;
        }}
        header {{
            background: #fff;
            padding: 24px;
            border-bottom: 1px solid #ddd;
        }}
        main {{
            max-width: 1000px;
            margin: auto;
            padding: 24px;
            background: #fff;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 24px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: center;
        }}
        th {{
            background: #f0f0f0;
        }}
        img {{
            max-width: 100px;
            border-radius: 8px;
        }}
        .button {{
            display: inline-block;
            padding: 8px 12px;
            background: #333;
            color: #fff;
            text-decoration: none;
            border-radius: 6px;
        }}
        .note {{
            font-size: 0.9em;
            color: #666;
        }}
    </style>
</head>
<body>
<header>
    <h1>無添加ベーコンおすすめ比較</h1>
    <p>価格・口コミ・レビュー件数をもとに、無添加ベーコンを比較します。</p>
</header>

<main>
    <h2>比較表</h2>

    <table>
        <thead>
            <tr>
                <th>順位</th>
                <th>画像</th>
                <th>商品名</th>
                <th>ショップ</th>
                <th>価格</th>
                <th>評価</th>
                <th>レビュー</th>
                <th>リンク</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>

    <h2>選び方</h2>
    <p>無添加ベーコンを選ぶときは、原材料、価格、レビュー数、送料を確認するのがおすすめです。</p>

    <p class="note">価格・在庫・レビュー情報は変動します。購入前に販売ページで最新情報を確認してください。</p>
</main>
</body>
</html>
"""

    Path(OUTPUT_FILE).write_text(html, encoding="utf-8")


def main():
    products = load_products()
    generate_html(products)
    print("index.htmlを生成しました。")


if __name__ == "__main__":
    main()