function isLocalStorageAvailable() {
    try {
        let storage = window.localStorage;
        let test = '__storage_test__';
        storage.setItem(test, test);
        storage.removeItem(test);
        return true;
    }
    catch(error) {
        return false;
    }
}

if (isLocalStorageAvailable()) {
    if ('scrollRestoration' in history) {
        history.scrollRestoration = 'manual'; /* отключает автопрокрутку браузером*/
    }

    window.addEventListener("load", event => {
        let answer = confirm("Чи дозволяєте ви використовувати локальне сховище?");

        if (answer) {
            window.scrollTo(0, window.localStorage["scrollTopPosition"] ?? 0);

            window.addEventListener("beforeunload", event => {
                /* Проверка долистали ли до конца страницы*/
                if (window.pageYOffset + window.innerHeight >= document.body.offsetHeight) {
                    window.localStorage.removeItem("scrollTopPosition");
                } else {
                    window.localStorage["scrollTopPosition"] = window.pageYOffset;
                }
            });
        }
    });

}
else {
    alert("Локальне сховище недоступне.");
}


