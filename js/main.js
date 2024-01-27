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

// Make the theme switcher in the hamburger menu on mobile devices work.
if (document.body.clientWidth < 940) {
	const themeSwitcherLabel = document.getElementById('main-theme-switcher');
	const navActionsContainer = document.getElementById('nav-actions-container');

	// Move the theme switcher to inside the hamburger menu.
	navActionsContainer.appendChild(themeSwitcher);
	navActionsContainer.appendChild(themeSwitcherLabel);

	themeSwitcherLabel.style.top = '';
	themeSwitcherLabel.style.left = '42vw';

	const themeVariables = [
		// Light theme
		[
			{ name: 'primary-color', value: '#666666' },
			{ name: 'secondary-color', value: '#555555' },
			{ name: 'font-color', value: '#555555' },
			{ name: 'link-color', value: '#444444' },
			{ name: 'bg-color', value: '#f0f0f0' },
			{ name: 'heading-color', value: '#666666' },
			{ name: 'block-bg-color', value: '#d7d7d7' },
			{ name: 'block-bg-color-secondary', value: '#c0c0c0' },
			{ name: 'block-bg-color-heading', value: '#a5a5a5' },
			{ name: 'table-color', value: '#000000' },
			{ name: 'head-nav-bg-color', value: 'transparent' },
			{ name: 'head-nav-text-color', value: '#d56f2a' },
			{ name: 'menu-color', value: '#202225' },
			{ name: 'license-color', value: '#666666' },
		],

		// Dark theme
		[
			{ name: 'primary-color', value: '#888888' },
			{ name: 'secondary-color', value: '#666666' },
			{ name: 'font-color', value: '#cecece' },
			{ name: 'link-color', value: '#e6e6e6' },
			{ name: 'bg-color', value: '#0f0f0f' },
			{ name: 'heading-color', value: '#454545' },
			{ name: 'block-bg-color', value: '#2f3234' },
			{ name: 'block-bg-color-secondary', value: '#444444' },
			{ name: 'block-bg-color-heading', value: '#333333' },
			{ name: 'table-color', value: '#cecece' },
			{ name: 'head-nav-bg-color', value: 'transparent' },
			{ name: 'head-nav-text-color', value: '#d56f2a' },
			{ name: 'menu-color', value: '#e1e1e1' },
			{ name: 'license-color', value: '#666666' },
		]
	]

	const checkMobileTheme = () => {
		const theme = themeVariables[themeSwitcher.checked ? 1 : 0];

		theme.forEach(variable => {
			document.documentElement.style.setProperty(`--${variable.name}`, variable.value);
		});
	};

	// Ensure IE compatibility
	if (document.addEventListener) {
		themeSwitcher.addEventListener('change', checkMobileTheme);
	} else if (document.attachEvent) {
		themeSwitcher.attachEvent('onchange', checkMobileTheme);
	}

	checkMobileTheme();
}