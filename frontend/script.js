document.addEventListener("DOMContentLoaded", () => {
  const addBookForm = document.getElementById("addBookForm");
  const booksList = document.getElementById("booksList");
  const searchInput = document.getElementById("searchInput");
  const searchButton = document.getElementById("searchButton");
  const message = document.getElementById("message");

  let books = [];

  // Adaugă o carte
  addBookForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    const genre = document.getElementById("genre").value;
    const year = document.getElementById("year").value;
    const status = document.getElementById("status").value;

    const newBook = { title, author, genre, year, status };
    books.push(newBook);
    displayBooks();
    addBookForm.reset();
    message.textContent = "Cartea a fost adăugată cu succes!";
  });

  // Afișează cărțile
  function displayBooks() {
    booksList.innerHTML = "";
    books.forEach((book, index) => {
      const li = document.createElement("li");
      li.textContent = `${book.title} de ${book.author} (${book.year}) - Stare: ${book.status}`;
      booksList.appendChild(li);
    });
  }

  // Căutare cărți
  searchButton.addEventListener("click", () => {
    const keyword = searchInput.value.toLowerCase();
    const results = books.filter(
      (book) =>
        book.title.toLowerCase().includes(keyword) ||
        book.author.toLowerCase().includes(keyword)
    );
    booksList.innerHTML = "";
    if (results.length > 0) {
      results.forEach((book) => {
        const li = document.createElement("li");
        li.textContent = `${book.title} de ${book.author} (${book.year}) - Stare: ${book.status}`;
        booksList.appendChild(li);
      });
    } else {
      booksList.innerHTML = "Nu au fost găsite cărți.";
    }
  });
});
