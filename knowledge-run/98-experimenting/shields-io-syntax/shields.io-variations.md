# 🛡️ Experimenting with Badges at Shields.io

This is a quick guide on how to build and implement dynamic badges for GitHub documentation.

## 1. The Basic URL Structure
To create a badge, use the following base URL:
`https://img.shields.io/badge/Label-Message-Color`

### Implementation in Markdown:
Input the link inside the standard image syntax:  
`![Alt Text](URL_Link)`

![Basic Badge](https://img.shields.io/badge/one_message-yellow)

---

## 2. URL Orthography (Crucial)
Since badges are generated via URLs, characters matter. Use these "translations":

* **Space:** Use an underscore `_` or `%20`.
* **Dash (-):** Use a double dash `--`.
* **Underscore (_):** Use a double underscore `__`.
* **Percentage (%):** Use `%25`.

![Orthography Test](https://img.shields.io/badge/one_message-followed_by_other-yellow)

---

## 3. Changing Styles
Modify the visual "vibe" using the `?style=` parameter.

* **Flat (Default):** ![Flat](https://img.shields.io/badge/Your_coverage-95%25-orange?style=flat)
* **Flat-Square:** ![Flat-Square](https://img.shields.io/badge/Your_coverage-95%25-orange?style=flat-square)
* **For the Badge:** ![For-the-badge](https://img.shields.io/badge/NEW_TEST-PASSED-brightgreen?style=for-the-badge)
* **Plastic:** ![Plastic](https://img.shields.io/badge/Your_coverage-95%25-orange?style=plastic)
* **Social:** ![Social](https://img.shields.io/badge/Your_coverage-95%25-orange?style=social)

---

## 4. Icons & Advanced Customization
Integrate logos from [Simple Icons](https://simpleicons.org/) using the `?logo=` parameter.

* **With Logo:** ![GitHub Logo](https://img.shields.io/badge/github-repo-blue?logo=github)
* **Advanced Formatting:** Combine `logoColor`, `labelColor`, and `color`.
    
![Advanced](https://img.shields.io/badge/Meu%20nome%20é-douglas-white?style=plastic&logo=autocad&logoColor=white&labelColor=red&color=yellow)

## 5. Adding Clickable Urls
<a href="https://SEU_LINK_AQUI.com" target="_blank">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Meu Perfil Python">
</a>

---

## 6. Design Scaneability
wrong: hi i develop on python!

correct: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">