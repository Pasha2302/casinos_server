

const startParserAPI = (_method, query_data = null) => {
  const requestUrls = {
    POST: "/api/v1/start-parser/",
    GET: `/api/v1/start-parser/`,
  };

  let requestOptions = {
    method: _method,
    headers: {
      "Content-Type": "application/json",
      // "X-CSRFToken": csrf_token,
    },
  };

  if (_method === "POST" || _method === "PUT") {
    const dataToSave = { name: casinoName, data: query_data };
    requestOptions.body = JSON.stringify(dataToSave);
  }

  return new Promise((resolve, reject) => {
    fetch(requestUrls[_method], requestOptions)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        resolve(data);
      })
      .catch((error) => {
        console.error(
          "!!! There was a problem saving/retrieving the data:",
          error
        );
        reject(error);
      });
  });
};


const creatButtonStartParser = () => {
  const checkButton = document.querySelector("#start-parser");
  const targetElement = document.querySelector("#toolbar");

  if (!checkButton && targetElement) {
    const info = document.createElement("span");
    info.setAttribute("class", "info-pars");
    info.textContent = "Data collection started";

    const buttonElement = document.createElement("button");
    buttonElement.setAttribute("id", "start-parser");
    buttonElement.setAttribute("class", "button-pars");
    buttonElement.setAttribute("type", "button");
    buttonElement.textContent = "Start Parser Data Casinos";

    targetElement.appendChild(buttonElement);
    buttonElement.appendChild(info);

    buttonElement.addEventListener("click", () => {
      info.classList.add("show");

      startParserAPI("GET")
        .then((data) => {
          console.log("\nData Parser From Server:", data);
          info.textContent = data.message;
        })
        .catch((err) => {
          info.textContent = `Произошла ошибка !!! ${err}`;
        });

      setTimeout(() => {
        info.style.opacity = 1;
      }, 10);

      setTimeout(() => {
        info.style.opacity = 0;
        setTimeout(() => {
          info.classList.remove("show");
        }, 2000); // Время должно совпадать с transition в CSS
      }, 4000); // Время, через которое элемент начнет исчезать
    });
  }
};


$(document).ready(function () {
  creatButtonStartParser();
});
