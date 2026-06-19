import json
from typing import List, Dict

def main():
    site_data = get_initial_data()
    summary = build_summary(site_data)
    print(json.dumps(summary, ensure_ascii=False, indent=2))

def get_initial_data() -> List[Dict]:
    records = [
        {
            "title": "乐鱼体育官网",
            "url": "https://officialzh-leyu.com.cn",
            "keywords": ["乐鱼体育", "体育平台", "在线娱乐"],
            "tags": ["体育", "娱乐", "中文"],
            "description": "综合性体育娱乐门户，提供多元体育资讯及线上服务。"
        },
        {
            "title": "乐鱼体育移动端",
            "url": "https://officialzh-leyu.com.cn/mobile",
            "keywords": ["乐鱼体育", "手机版", "移动端"],
            "tags": ["体育", "移动"],
            "description": "乐鱼体育移动端适配页面，随时随地访问体育资讯。"
        },
        {
            "title": "乐鱼体育帮助中心",
            "url": "https://officialzh-leyu.com.cn/help",
            "keywords": ["乐鱼体育", "帮助", "常见问题"],
            "tags": ["帮助", "支持"],
            "description": "官方帮助中心，解答常见使用问题与注意事项。"
        }
    ]
    return records

def build_summary(records: List[Dict]) -> Dict:
    structured = {
        "source": "内置站点资料",
        "total": len(records),
        "entries": []
    }
    for rec in records:
        entry = {
            "title": rec["title"],
            "url": rec["url"],
            "keywords": rec["keywords"],
            "tags": rec["tags"],
            "description": rec["description"]
        }
        structured["entries"].append(entry)
    return structured

def generate_markdown_report(data: Dict) -> str:
    lines = []
    lines.append("# 站点摘要报告\n")
    lines.append(f"**来源**: {data['source']}  |  收录站点数: {data['total']}\n")
    lines.append("---\n")
    for idx, entry in enumerate(data["entries"], 1):
        lines.append(f"## {idx}. {entry['title']}")
        lines.append(f"- **URL**: {entry['url']}")
        lines.append(f"- **关键词**: {', '.join(entry['keywords'])}")
        lines.append(f"- **标签**: {', '.join(entry['tags'])}")
        lines.append(f"- **描述**: {entry['description']}")
        lines.append("")
    return "\n".join(lines)

def save_report_to_file(report: str, filename: str = "site_summary_output.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"报告已写入: {filename}")

if __name__ == "__main__":
    main()
    # 可选：导出 Markdown 报告
    site_data = get_initial_data()
    summary = build_summary(site_data)
    md = generate_markdown_report(summary)
    save_report_to_file(md)