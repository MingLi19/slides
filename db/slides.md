---
theme: seriph
background: https://cover.sli.dev
title: 海洋大数据技术
class: text-center
drawings:
  persist: false
transition: slide-left
codeCopy: true
mdc: true
---

# NoSQL数据库

上海海事大学 - 2024.10

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Let's rock 🤘<carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/MingLi19/slides" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>
---

# 课程大纲

<Toc v-click columns="2" minDepth="2" maxDepth="2"></Toc>

---

### NoSQL兴起背景

<img v-click class="w-100 p-4" border="rounded" src="./images/noSQL.png" alt="noSQL">

---

### 关系型数据库
<br>  
<v-switch>
  <template #1> 
    - 固定的表结构：表、行、列 
    <img class="w-100 p-4" border="rounded" src="./images/rmdb_demo.png" alt="noSQL">
  </template>
  <template #2> 
    - 固定的表结构：表、行、列
    <br>
    - 高效的查询处理
  </template>
  <template #3> 
    - 固定的表结构：表、行、列
    <br>
    - 高效的查询处理
    <br>
    - 完善的事务管理机制
  </template>
</v-switch>

---
layout: two-cols
layoutClass: gap-8
---

## 数据库概览

<br />

<img class="w-100" border="rounded" src="./images/db_rank.png" alt="db_rank">

来源于 [DB-engines](https://db-engines.com/en/ranking)

::right::

<img v-click class="w-100" border="rounded" src="./images/db_map.jpeg" alt="db_map">



---
src: ./pages/mongodb.md 
---
---
src: ./pages/redis.md
---
src: ./pages/neo4j.md
---