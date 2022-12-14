// SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
// SPDX-License-Identifier: MIT

window.onload = () => {
    let url = "https://api.github.com/repos/RailwayController/dev-docs/commits/main";
    let copyright = document.getElementById("copyright")

    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            let shortHash = data.sha.substring(0, 7)
            let container = document.createElement("div")
            container.append("Revision ")
            let link = document.createElement("a")
            link.href = data.html_url
            link.innerHTML = shortHash
            container.append(link)
            copyright.after(container)
        })
}