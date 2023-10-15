// Saves themes in-between pages to LocalStorage.
const themeSwitcher = document.getElementById('theme-switcher');

const setTheme = e => localStorage.setItem('theme', e.target.checked ? 'dark' : 'light');
const checkTheme = () => themeSwitcher.checked = localStorage.getItem('theme') === 'dark';

// Ensures backward compatibility with IE old versions
if (document.addEventListener) {
	themeSwitcher.addEventListener('click', setTheme);
} else if (document.attachEvent) {
	themeSwitcher.attachEvent('onclick', setTheme);
}

checkTheme()