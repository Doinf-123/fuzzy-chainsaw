window.onload = () => {
    const button = document.querySelector('#btn');
    button.addEventListener('click', calculateBmi);
}

function calculateBmi() {
    const height = parseFloat(document.querySelector('#height').value);
    const weight = parseFloat(document.querySelector('#weight').value);
    const result = document.querySelector('#result');

    if (!height || isNaN(height) || height < 0) {
        result.innerText = "Please enter a valid height";
        return;
    } else if (!weight || isNaN(weight) || weight < 0) {
        result.innerText = "Please enter a valid weight";
        return;
    }

    const BMI = (weight / (height * height)).toFixed(2);

    if (BMI < 18.5) {
        result.innerText = `Under Weight: ${BMI}`;
    } else if (BMI >= 18.5 && BMI < 24.9) {
        result.innerText = `Normal: ${BMI}`;
    } else if (BMI >= 25 && BMI < 29.9) {
        result.innerText = `Over Weight: ${BMI}`;
    } else if (BMI >= 30 && BMI < 34.9) {
        result.innerText = `Obesity (Class 1): ${BMI}`;
    } else if (BMI >= 35 && BMI < 39.9) { // Changed 35.5 to 35
        result.innerText = `Obesity (Class 2): ${BMI}`;
    } else {
        result.innerText = `Extreme Obesity: ${BMI}`;
    }
}

