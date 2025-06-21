---
layout: home
title: Clover-Clever의 기술 블로그
---

# 🧲⚡🚀 Clover-Clever의 기술 블로그

**Formula Student, 인버터, BMS, 전력전자, 드론 제어 개발 기록 블로그입니다.**  
하드웨어 설계부터 제어 알고리즘까지 모든 여정을 기록합니다.

---

## 💡 주요 관심 분야

- 🔋 **전력전자** (인버터, SiC/GaN 기반 회로 설계)
- ⚙️ **모터 제어** (FOC, 센서리스 제어)
- 🧠 **드론** 및 삼중 육·해·공 드론 플랫폼 설계
- 🛠️ **BMS 알고리즘** 및 하드웨어 개발
- 💻 **임베디드 시스템** (STM32, ATmega, TC275)
- 📐 **회로/기구 설계 & 시뮬레이션** (KiCad, MATLAB, CATIA V5)

---

## 📝 최근 글

<ul>
  {% for post in paginator.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">
        {{ post.title }} <small>({{ post.date | date: "%Y-%m-%d" }})</small>
      </a>
    </li>
  {% endfor %}
</ul>

> 📌 더 많은 글은 [블로그 전체 보기]({{ site.paginate_path | replace: ':num', '1' }})에서 확인하실 수 있습니다.

---

## 🔗 외부 링크

- 💼 [GitHub 프로필](https://github.com/clover-clever)
- 🏁 [한양대 Formula Student 팀 RACE](https://www.racehanyang.com/)

---

<div align="center">
  <sub>© 2025 Sanghoon Lee – Powered by <a href="https://github.com/bitbrain/jekyll-dash">jekyll-dash</a></sub>
</div>
