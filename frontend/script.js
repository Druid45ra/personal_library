document.addEventListener("DOMContentLoaded", function () {
  loadBooks();

  // Adăugarea unei cărți
  const addBookForm = document.getElementById("add-book-form");
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
      .then((response) => response.json())
      .then((data) => {
        loadBooks(); // Reîncarcă lista de cărți
        addBookForm.reset();
      });
  });
});
