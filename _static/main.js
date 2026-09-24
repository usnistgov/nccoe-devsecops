(function () {
    function scrollToCurrentFragment() {
        if (!window.location.hash) {
            return;
        }

        const target = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
        if (!target) {
            return;
        }

        window.requestAnimationFrame(function () {
            window.requestAnimationFrame(function () {
                target.scrollIntoView({ block: "start" });
            });
        });
    }

    window.addEventListener(
        "load",
        function () {
            scrollToCurrentFragment();
        },
        { once: true }
    );
})();
