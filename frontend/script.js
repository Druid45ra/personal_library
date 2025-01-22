document.addEventListener("DOMContentLoaded", function () {
  loadBooks();

  const messageDiv = document.getElementById("message");

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

    const validateBook = (book) => {
      if (!book.title || !book.author || !book.genre || !book.year || !book.status) {
        messageDiv.textContent = "Toate câmpurile sunt obligatorii!";
        return false;
      }
      return true;
    };

    if (!validateBook(book)) {
      return;
    }

    fetch("/books", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(book),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to add book");
        }
        return response.json();
      })
      .then((data) => {
        loadBooks(); // Reîncarcă lista de cărți
        addBookForm.reset();
        messageDiv.textContent = "Cartea a fost adăugată cu succes!";
      })
      .catch((error) => {
        messageDiv.textContent = error.message;
      });
  });
});     messageDiv.textContent = "Cartea a fost adăugată cu succes!";
      })
      .catch((error) => {
        messageDiv.textContent = error.message;
      });
  });
});
