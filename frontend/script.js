document.addEventListener("DOMContentLoaded", function () {
  loadBooks();

  const messageDiv = document.getElementById("message");

  // Funcție pentru a afișa mesajele
  const showMessage = (message, isSuccess = true) => {
    messageDiv.textContent = message;
    messageDiv.style.color = isSuccess ? "green" : "red";
  };

  // Adăugarea unei cărți
  const addBookForm = document.getElementById("addBookForm");
  addBookForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const titleInput = document.getElementById("title");
    const authorInput = document.getElementById("author");
    const genreInput = document.getElementById("genre");
    const yearInput = document.getElementById("year");
    const statusInput = document.getElementById("status");

    const book = {
      title: titleInput.value.trim(),
      author: authorInput.value.trim(),
      genre: genreInput.value.trim(),
      year: yearInput.value.trim(),
      status: statusInput.value.trim(),
    };

    // Validare câmpuri
    const validateBook = (book) => {
      if (
        !book.title ||
        !book.author ||
        !book.genre ||
        !book.year ||
        !book.status
      ) {
        showMessage("Toate câmpurile sunt obligatorii!", false);
        return false;
      }
      if (isNaN(book.year) || parseInt(book.year) < 0) {
        showMessage("Anul trebuie să fie un număr pozitiv!", false);
        return false;
      }
      return true;
    };

    if (!validateBook(book)) {
      return;
    }

    fetch("http://127.0.0.1:5000/books", {
      // Asigură-te că serverul este activ pe acest port
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(book),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Eroare la adăugarea cărții!");
        }
        return response.json();
      })
      .then((data) => {
        loadBooks(); // Reîncarcă lista de cărți
        addBookForm.reset();
        showMessage("Cartea a fost adăugată cu succes!");
      })
      .catch((error) => {
        showMessage(error.message, false);
      });
  });

  // Funcție pentru încărcarea cărților
  function loadBooks() {
    fetch("http://127.0.0.1:5000/books") // Asigură-te că serverul este activ pe acest port
      .then((response) => {
        if (!response.ok) {
          throw new Error("Eroare la încărcarea cărților!");
        }
        return response.json();
      })
      .then((books) => {
        const booksList = document.getElementById("booksList");
        booksList.innerHTML = ""; // Curăță lista existentă

        books.forEach((book) => {
          const li = document.createElement("li");
          li.textContent = `${book.title} - ${book.author} (${book.year})`;
          booksList.appendChild(li);
        });
      })
      .catch((error) => {
        showMessage(error.message, false);
      });
  }
});
