#from pydoc import classname
import time
import streamlit as st
import tensorflow as tf
import numpy as np
import os

# Add an image banner at the top
banner_image = r"D:\yashu\MCA\Skin Disease Detection\banner.png"  # Replace with the path to your banner image
st.image(banner_image, use_column_width=True)

st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;  /* Light Blue */
        }
        .navbar {
            background-color: #2E8B57;  /* Sea Green */
            padding: 10px;
            text-align: center;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            margin: 0 20px;
            font-size: 18px;
        }
        .navbar a:hover {
            background-color: #4a1162;
            padding: 10px;
        }
        .stButton button {
            border: 2px solid #E6E6FA;  /* Border color */
            border-radius: 5px;         /* Border radius for rounded corners */
            padding: 10px 20px;         /* Padding inside the button */
            background-color: #6A0DAD;  /* Background color */
            color: white;               /* Text color */
            font-size: 16px;            /* Font size */
        }
        st.progress{
            color:#6A4C9C;
            }
        .stButton button:hover {
            background-color: #6A4C9C;  /* Hover background color */
            border: 2px solid #6A0DAD;
            color:black;
        }
        st.file_uploader {
            border: 2px solid #6A4C9C; /* Dark Lavender border */
            padding: 5px;
            border-radius: 8px;
            background-color: #f5f5f5; /* Light background */
        }

        st.file_uploader:hover {
            border: 2px solid #4E3C80; /* Darker lavender on hover */
        }

    """, unsafe_allow_html=True)

# Top navbar with page links
app_mode = st.selectbox("SkinXpert AI", ["Disease Recognition", "Disease info","Preventions"])
classname = ["Acne", "Cellulitis Impetigo","Eczema","Healthy Skin", "Melanoma","Vascular Tumors", "Vitiligo" ,"Warts"]


# TensorFlow model prediction function
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(150, 150))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # return index of max element

# Disease Recognition Page
if app_mode == "Disease Recognition":
    st.header("Disease Recognition ")
    test_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

    if st.button("✨ Predict Now!"):
        with st.spinner("Analyzing..."):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
        st.success("Prediction Complete!")

        if test_image:
            st.image(test_image, width=200)
            result_index = model_prediction(test_image)
            predicted_disease = classname[result_index]
            st.success(f"Predicted Condition: **{predicted_disease}**")

# Diseases Page
elif app_mode == "Disease info":
    st.header("Diseases Information")
    app_mode2 = st.selectbox("Select Disease", ['Acne', 'Cellulitis Impetigo', 'Eczema', 'Healthy Skin', 'Melanoma Nevi and Moles', 'Vascular Tumors', 'Vitiligo'])
    
    if app_mode2 == "Acne":
        st.header("Acne")
        st.markdown("""
        ### What is Acne?
        Acne is a common skin condition that occurs when hair follicles become clogged with oil, dead skin cells, and bacteria.
        **Symptoms of Acne**:
        - Blackheads
        - Whiteheads
        - Papules
        - Pustules
        - Cysts or Nodules
        """)

    elif app_mode2 == "Cellulitis Impetigo":
        st.header("Cellulitis Impetigo")
        st.markdown("""
        ### What is Cellulitis Impetigo?
        Cellulitis is a bacterial skin infection, while impetigo is a superficial skin infection that often affects children.
        **Symptoms of Cellulitis Impetigo**:
        - Redness and swelling
        - Pain or tenderness
        - Blisters
        """)

    elif app_mode2 == "Eczema":
        st.header("Eczema")
        st.markdown("""
        ### What is Eczema?
        Eczema is a condition that makes the skin inflamed or irritated. It often causes itchiness and redness.
        **Symptoms of Eczema**:
        - Dry skin
        - Itching
        - Red rash
        """)

    elif app_mode2 == "Healthy Skin":
        st.header("Healthy Skin")
        st.markdown("""
        ### What is Healthy Skin?
        Healthy skin is well-hydrated, with a good barrier function that protects from harmful elements.
        **Signs of Healthy Skin**:
        - Smooth and hydrated
        - Even tone
        - No rashes or irritation
        """)

    elif app_mode2 == "Melanoma Nevi and Moles":
        st.header("Melanoma Nevi and Moles")
        st.markdown("""
        ### What is Melanoma?
        Melanoma is a type of skin cancer that originates in melanocytes. Nevi (moles) can become melanoma.
        **Symptoms of Melanoma**:
        - Irregular mole shape
        - Change in size or color
        - Bleeding or itching
        """)

    elif app_mode2 == "Vascular Tumors":
        st.header("Vascular Tumors")
        st.markdown("""
        ### What are Vascular Tumors?
        Vascular tumors are growths formed by blood vessels and can be benign or malignant.
        **Symptoms of Vascular Tumors**:
        - Red or purple raised skin lesions
        - Bruising or swelling
        """)

    elif app_mode2 == "Vitiligo":
        st.header("Vitiligo")
        st.markdown("""
        ### What is Vitiligo?
        Vitiligo is a condition where the skin loses its pigment, leading to lighter patches of skin.
        **Symptoms of Vitiligo**:
        - White patches on the skin
        - Premature graying of hair
        """)

    elif app_mode2 == "Warts Molluscum":
        st.header("Warts Molluscum")
        st.markdown("""
        ### What is Warts Molluscum?
        Warts are growths caused by a viral infection, while molluscum contagiosum is a viral infection causing small bumps.
        **Symptoms of Warts Molluscum**:
        - Small, raised bumps
        - White or flesh-colored lesions
        - Itchy or irritated skin
        """)

elif app_mode == "Preventions":
    st.header("Preventions")
    app_mode3 = st.selectbox("Select Disease", ['Acne', 'Cellulitis Impetigo', 'Eczema', 'Healthy Skin', 'Melanoma Nevi and Moles', 'Vascular Tumors', 'Vitiligo'])

    if app_mode3 == "Acne":
        st.header("Acne")
        st.markdown("""
        ### What is Acne?
        Acne is a common skin condition that occurs when hair follicles become clogged with oil, dead skin cells, and bacteria.

        **Symptoms of Acne**:
        - Blackheads
        - Whiteheads
        - Papules
        - Pustules
        - Cysts or Nodules

        **Preventions**:
        1. **Maintain a Consistent Skincare Routine**:
           - Wash your face twice daily with a gentle, non-comedogenic cleanser to remove excess oil and dirt.
           - Avoid harsh scrubbing, which can irritate the skin.

        2. **Use Acne-Fighting Products**:
           - Choose products containing **salicylic acid**, **benzoyl peroxide**, or **retinoids** to clear clogged pores.

        3. **Moisturize**:
           - Even oily skin needs hydration; use an oil-free, non-comedogenic moisturizer.

        4. **Avoid Touching Your Face**:
           - Prevent transferring bacteria by keeping your hands off your face.

        5. **Manage Diet and Stress**:
           - Reduce intake of sugary and high-glycemic foods.
           - Practice stress-relief techniques like yoga or meditation.
        """)

    elif app_mode3 == "Cellulitis Impetigo":
        st.header("Cellulitis Impetigo")
        st.markdown("""
        ### What is Cellulitis Impetigo?
        Cellulitis is a bacterial skin infection, while impetigo is a superficial infection often affecting children.

        **Symptoms of Cellulitis Impetigo**:
        - Redness and swelling
        - Pain or tenderness
        - Blisters

        **Preventions**:
        1. **Practice Good Hygiene**:
           - Wash hands regularly with soap to reduce bacterial spread.

        2. **Care for Wounds Properly**:
           - Clean cuts or scrapes immediately, apply antiseptic, and cover with a bandage.

        3. **Avoid Sharing Personal Items**:
           - Do not share towels, razors, or other personal items to prevent bacterial transmission.

        4. **Strengthen the Immune System**:
           - Eat a healthy diet rich in vitamins, especially vitamin C, to support immune function.
        """)

    elif app_mode3 == "Eczema":
        st.header("Eczema")
        st.markdown("""
        ### What is Eczema?
        Eczema is a condition that causes skin inflammation, leading to itchiness and redness.

        **Symptoms of Eczema**:
        - Dry skin
        - Itching
        - Red rash

        **Preventions**:
        1. **Moisturize Regularly**:
           - Use fragrance-free moisturizers immediately after bathing to lock in moisture.

        2. **Avoid Triggers**:
           - Identify and avoid triggers like allergens, harsh soaps, or temperature extremes.

        3. **Wear Soft Fabrics**:
           - Choose breathable, soft materials like cotton instead of wool or synthetics.

        4. **Manage Stress**:
           - Use stress management techniques, as stress can exacerbate eczema.
        """)

    elif app_mode3 == "Healthy Skin":
        st.header("Healthy Skin")
        st.markdown("""
        ### What is Healthy Skin?
        Healthy skin is well-hydrated and has a good barrier function, protecting against harmful elements.

        **Signs of Healthy Skin**:
        - Smooth and hydrated
        - Even tone
        - No rashes or irritation

        **Preventions**:
        1. **Hydrate and Eat a Balanced Diet**:
           - Drink plenty of water and eat foods rich in vitamins A, C, and E.

        2. **Use Sunscreen Daily**:
           - Apply broad-spectrum SPF 30+ sunscreen to protect against UV damage.

        3. **Follow a Skincare Routine**:
           - Cleanse, moisturize, and exfoliate regularly using products suitable for your skin type.

        4. **Sleep and Stress Management**:
           - Get 7–8 hours of sleep and practice stress-reducing activities like meditation.
        """)

    elif app_mode3 == "Melanoma Nevi and Moles":
        st.header("Melanoma Nevi and Moles")
        st.markdown("""
        ### What is Melanoma?
        Melanoma is a type of skin cancer originating in melanocytes. Moles (nevi) can develop into melanoma.

        **Symptoms of Melanoma**:
        - Irregular mole shape
        - Change in size or color
        - Bleeding or itching

        **Preventions**:
        1. **Use Sunscreen**:
           - Apply a broad-spectrum SPF 30+ sunscreen daily, even on cloudy days.

        2. **Avoid Excessive Sun Exposure**:
           - Stay in the shade, especially between 10 AM and 4 PM.

        3. **Regular Skin Checks**:
           - Monitor moles for any changes and consult a dermatologist annually.

        4. **Avoid Tanning Beds**:
           - Tanning beds increase the risk of melanoma, so avoid them completely.
        """)

    elif app_mode3 == "Vascular Tumors":
        st.header("Vascular Tumors")
        st.markdown("""
        ### What are Vascular Tumors?
        Vascular tumors are growths formed by blood vessels and can be benign or malignant.

        **Symptoms of Vascular Tumors**:
        - Red or purple raised skin lesions
        - Bruising or swelling

        **Preventions**:
        1. **Protect Skin from Injury**:
           - Avoid trauma to the skin to reduce the chance of abnormal vessel growth.

        2. **General Health Maintenance**:
           - Maintain overall good health through a balanced diet and regular check-ups.
        """)

    elif app_mode3 == "Vitiligo":
        st.header("Vitiligo")
        st.markdown("""
        ### What is Vitiligo?
        Vitiligo is a condition where the skin loses its pigment, resulting in white patches.

        **Symptoms of Vitiligo**:
        - White patches on the skin
        - Premature graying of hair

        **Preventions**:
        1. **Protect Skin from Sun Exposure**:
           - Use sunscreen to protect depigmented areas and prevent burns.

        2. **Avoid Skin Trauma**:
           - Minimize skin injuries, burns, and cuts to reduce the risk of new patches forming.

        3. **Healthy Lifestyle**:
           - Maintain a nutritious diet and manage stress to support immune health.
        """)
