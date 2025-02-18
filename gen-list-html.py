#!/usr/bin/env python3

import sqlite3
import os


# 获取数据库中所有表的数据
def fetch_table_data(db: str) -> dict:
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row  # 使得查询结果可以通过列名访问
    cursor = conn.cursor()

    # 获取数据库中的所有表
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # 获取每个表的内容
    table_data = {}
    for table in tables:
        table_name = table["name"]
        cursor.execute(f"SELECT * FROM {table_name}")
        table_data[table_name] = cursor.fetchall()

    conn.close()
    return table_data


# 生成静态 HTML 页面
def generate_html(table_data, filename):
    html = """<!doctype html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="color-scheme" content="light dark">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>仓库内容</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .tabs {
            overflow: hidden;
            background-color: #f1f1f1;
        }
        .tabs button {
            background-color: #ddd;
            border: none;
            display: inline-block;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .tabs button:hover {
            background-color: #ccc;
        }
        .tabs button.active {
            background-color: #3498db;
            color: white;
        }
        .tab-content {
            display: none;
            padding: 20px;
            border-top: 2px solid #ddd;
        }
        .tab-content.active {
            display: block;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        /* 增加水平滚动条的样式 */
        .table-wrapper {
            overflow-x: auto;  /* 启用水平滚动 */
            -webkit-overflow-scrolling: touch;  /* 提升在触控设备上的滚动体验 */
        }
    </style>
</head>
<body>
    <div class="tabs">"""

    # 创建标签栏
    for table_name in table_data.keys():
        html += f'<button class="tab-button" id="tab-{table_name}" onclick="showTab(\'{table_name}\')">{table_name}</button>'

    html += "</div>\n    "

    # 渲染每个表格的内容
    for table_name, rows in table_data.items():
        html += f'<div class="tab-content" id="content-{table_name}">'
        html += f"<h2>{table_name}</h2>"

        # 表格外层包裹 div，启用水平滚动
        html += '<div class="table-wrapper">'
        html += "<table>"

        # 表头
        if rows:
            html += "<tr>"
            for column in rows[0].keys():
                html += f"<th>{column}</th>"
            html += "</tr>"

            # 表格数据
            for row in rows:
                html += "<tr>"
                for column in row.keys():
                    html += f"<td>{row[column]}</td>"
                html += "</tr>"

        html += "</table>"
        html += "</div>"  # 结束 .table-wrapper
        html += "</div>"

    # 添加 JavaScript 以实现标签切换功能
    html += """
<script>
    function showTab(tableName) {
        // 隐藏所有 tab 内容
        var contents = document.querySelectorAll('.tab-content');
        contents.forEach(function(content) {
            content.classList.remove('active');
        });
        // 移除所有按钮的 active 类
        var buttons = document.querySelectorAll('.tab-button');
        buttons.forEach(function(button) {
            button.classList.remove('active');
        });
        // 显示当前选中的 tab 内容
        document.getElementById('content-' + tableName).classList.add('active');
        // 给当前按钮添加 active 类
        document.getElementById('tab-' + tableName).classList.add('active');
    }
    // 默认显示第一个表
    document.addEventListener('DOMContentLoaded', function() {
        var firstTable = document.querySelector('.tab-button');
        if (firstTable) {
            firstTable.click();
        }
    });
</script>
</body>
</html>
"""

    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.makedirs(dir)
    # 保存为静态 HTML 文件
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    db = "data/deb.db"
    filename="deb/list/index.html"
    table_data = fetch_table_data(db)
    generate_html(table_data, filename)
