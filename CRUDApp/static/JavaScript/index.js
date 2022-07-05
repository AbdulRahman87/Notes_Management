const title = /^[a-zA-Z]([ ]{0,1}[a-zA-Z]){3,50}[a-zA-Z]$/;
const inpTitle = document.getElementById('title');
const inpDesc = document.getElementById('desc');
const btn = document.getElementById('submitBtn');

inpTitle.addEventListener('blur', () => {
    if (title.test(inpTitle.value)) {
        inpTitle.classList.remove('is-invalid');
        btn.removeAttribute('disabled', 'disabled');
    }
    else {
        inpTitle.classList.add('is-invalid');
        btn.setAttribute('disabled', 'disabled');
    }
});

inpDesc.addEventListener('blur', () => {
    if (inpDesc.value.length < 5) {
        inpDesc.classList.add('is-invalid');
        btn.setAttribute('disabled', 'disabled')
    }
    else {
        inpDesc.classList.remove('is-invalid');
        btn.removeAttribute('disabled', 'disabled');
    }
});
