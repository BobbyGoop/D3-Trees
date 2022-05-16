const dropdowns = document.querySelectorAll('.dropdown');
dropdowns.forEach(dropdown => {
    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');
    select.addEventListener('click', () => {
        select.classList.toggle('select-clicked');
        caret.classList.toggle('caret-rotate');
        menu.classList.toggle('menu-open');
    });
    options.forEach(option => {
        option.addEventListener('click', () => {
            selected.innerText = option.innerText;
            if (selected.classList[1] === 'source') {
                document.getElementById('img_main').src = `../static/img/${selected.innerText}.png`;
            }
            if (selected.classList[1] === 'border') {
                console.log(selected.innerText)
                document.getElementById('img_main').style.border = `5px ${selected.innerText} solid`;
            }
            select.classList.remove('select-clicked');
            caret.classList.remove('caret-rotate');
            menu.classList.remove('menu-open');
            options.forEach(option => {
                option.classList.remove('active');
            });
            option.classList.add('active');
        });
    });
});

const popup = document.querySelector('.popup-image');
document.querySelectorAll('.img-gallery img').forEach(image => {
    image.onclick = () => {
      popup.style.display = 'block';
      document.querySelector('.popup-image img').src = image.getAttribute('src');
    };
});

 document.querySelector('.popup-image span').onclick = () => {
     popup.style.display = 'none';
 };

 document.querySelector('.feat-btn').onclick = () => {
      document.querySelector('.sidebar-wrapper ul .feat-show').classList.toggle("show");
 };

 document.querySelector('.serv-btn').onclick = () => {
      document.querySelector('.sidebar-wrapper ul .serv-show').classList.toggle("show1");
 };

 const menus = document.querySelectorAll('.sidebar-wrapper ul li');
 menus.forEach(menu => {
     menu.addEventListener('click', () => {
         menus.forEach(menu => {
             menu.classList.remove('side-active');
         });
         menu.classList.add('side-active');
     });
 });