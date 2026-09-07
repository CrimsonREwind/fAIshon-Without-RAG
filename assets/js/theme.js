
var themeKey = "faishon-theme";
var lightTheme = "lofi";
var darkTheme = "forest";

function readTheme() {
var savedTheme = darkTheme;
try {
    savedTheme = localStorage.getItem(themeKey) || darkTheme;
} catch (error) {
    savedTheme = darkTheme;
}

return savedTheme === lightTheme ? lightTheme : darkTheme;
}

function writeTheme(theme) {
document.documentElement.setAttribute("data-theme", theme);
try {
    localStorage.setItem(themeKey, theme);
} catch (error) {
    // Ignore storage failures and keep runtime theme.
}
}

function syncControllers(theme) {
var isDark = theme === darkTheme;
document.querySelectorAll(".theme-controller").forEach(function (controller) {
    controller.checked = isDark;
});
}

var initialTheme = readTheme();
writeTheme(initialTheme);
syncControllers(initialTheme);

document.querySelectorAll(".theme-controller").forEach(function (controller) {
controller.addEventListener("change", function () {
    var nextTheme = controller.checked ? darkTheme : lightTheme;
    writeTheme(nextTheme);
    syncControllers(nextTheme);
});
});

lucide.createIcons();


