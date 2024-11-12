import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Graph
from streamlit_echarts import st_echarts

st.set_page_config(
    page_title="sisiyuchichi",
    page_icon="🧊",
    layout="wide",
    menu_items=None
)

# 定义与中心节点相关的元素
elements = {
    "地点选择": ["经典浪漫", "日常特别", "冒险刺激"],
    "时间安排": ["日常惊喜", "节日庆典", "特殊纪念"],
    "氛围营造": ["自然美景", "装饰布置", "音乐陪伴"],
    "表白方式": ["直接表白", "创意表达", "游戏互动"],
    "礼物准备": ["实用礼物", "情感礼物", "体验礼物"]
}

# 创建节点和链接
nodes = []
links = []
categories = []

st.markdown("<h1 style='text-align: center; color: pink;'>What's on the menu?</h1>", unsafe_allow_html=True)



# 添加元素到节点和链接
category_index = 1
for category, items in elements.items():
    nodes.append({"name": category, "symbolSize": 40, "category": category_index})
    links.append({"source": "Love", "target": category})
    categories.append({"name": category})
    for item in items:
        nodes.append({"name": item, "symbolSize": 30, "category": category_index + len(elements)})
        links.append({"source": category, "target": item})
        categories.append({"name": item})
    category_index += 1

# 定义图表选项
option = {
    "backgroundColor": 'rgba(0, 0, 0, 0)',  # 设置背景色为透明

    "tooltip": {},
    "legend": [{"data": [cat["name"] for cat in categories if cat["name"] not in elements.keys()]}],  # 只保留最底层的标签
    "series": [
        {
            "name": "Love Framework",
            "type": "graph",
            "layout": "force",
            "data": nodes,
            "links": links,
            "categories": categories,
            "roam": True,
            "label": {"show": True, "position": "right", "formatter": "{b}"},
            "lineStyle": {"color": "source", "curveness": 0.3},
            "emphasis": {"focus": "adjacency", "lineStyle": {"width": 10}},
        }
    ],
}

# 在Streamlit中显示图表
st_echarts(option, height="400px")
st.markdown("<h4 style='text-align: center; color: pink;'>保留你想要的的元素，点击菜单可去除其他元素</h4>", unsafe_allow_html=True)