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
    Let's Go 🚀<carbon:arrow-right class="inline"/>
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

<Toc v-click columns="2" minDepth="2" maxDepth="3" mode="onlyCurrentTree"></Toc>

---
class: text-center
---

# SQL到NoSQL的转变

---
src: ./pages/nosql.md
---

---
class: text-center
---

# 文档数据库 - MongoDB

---
src: ./pages/mongodb.md
---

---
class: text-center
---

# 键值数据库 - Redis
---
src: ./pages/redis.md
---

---
class: text-center
---

# 图数据库 - Neo4j
---
src: ./pages/neo4j.md
---
