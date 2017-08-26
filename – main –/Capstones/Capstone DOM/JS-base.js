TicArray = document.querySelectorAll('th')

for (var i = 0; i < 9; i++) {
    var square = TicArray[i];
    square.addEventListener('click', function () {
            if (!this.textContent) {
                this.textContent = 'X';
            } else {
                if (this.textContent === 'O') {
                    this.textContent = '';
                } else {
                    this.textContent = 'O';
                }
            }
        });
    }