// @license magnet:?xt=urn:btih:d3d9a9a6595521f9666a5e94cc830dab83b65699&dn=expat.txt Expat
// The above is a GNU LibreJS specific license declaration. The Expat license is the same as the MIT license.
// See: https://www.gnu.org/software/librejs/free-your-javascript.html#magnet-link-license

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