document.addEventListener("DOMContentLoaded", function () {
  loadBooks();

  const messageDiv = document.getElementById("message");

  // Adăugarea unei cărți
  const addBookForm = document.getElementById("addBookForm");
  addBookForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const book = {
      title: document.getElementById("title").value,
      author: document.getElementById("author").value,
      genre: document.getElementById("genre").value,
      year: document.getElementById("year").value,
      status: document.getElementById("status").value,
    };

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
});
