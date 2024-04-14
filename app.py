import streamlit as st

def main():
    st.title("Indian Medicinal Plants Identifier")
    st.write("Upload an image of a plant to identify its medicinal plant name.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        # Placeholder result
        result = "neem"

        st.write("", "", "", result, "<style>div.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)
        st.write("")

        # Display additional information for neem
        st.header("Medicinal Content in Neem:")
        st.write(
            "Neem, scientifically known as Azadirachta indica, is a tree native to the Indian subcontinent and has been used in traditional medicine for centuries. Its medicinal properties primarily stem from various compounds found in its leaves, seeds, bark, and oil. Some of the key medicinal constituents include:"
        )

        # Display medicinal content in columns
        col1, col2 = st.columns(2)
        with col1:
            st.write("- Nimbin: Exhibits potent antifungal, antibacterial, and antiviral properties.")
            st.write("- Nimbidin: Acts as an anti-inflammatory agent.")
            st.write("- Quercetin: Possesses antioxidant and anti-inflammatory properties.")
            st.write("- Azadirachtin: Known for its insecticidal and antifungal properties.")
        with col2:
            st.write("- Epinimbin: Exhibits antimalarial properties.")
            st.write("- Gedunin: Shows potential as an anticancer agent.")

        st.header("Diseases Cured Using Neem:")
        st.write(
            "Neem is renowned for its versatile medicinal properties and is used in the treatment and prevention of various ailments, including:"
        )
        st.write("- Skin Disorders: Eczema, acne, psoriasis, and other dermatological conditions.")
        st.write("- Oral Health Issues: Gum disease, cavities, and oral infections.")
        st.write("- Digestive Disorders: Indigestion, ulcers, and intestinal worms.")
        st.write("- Immune System Support: Boosting immunity and combating infections.")
        st.write("- Insect Bites and Wounds: Relieving itching and promoting wound healing.")
        st.write("- Diabetes: Helping to regulate blood sugar levels.")
        st.write("- Malaria: Some compounds in neem exhibit antimalarial properties.")

        st.header("Age Restriction in Neem:")
        st.write(
            "Neem products such as neem oil or neem leaf extract are generally safe for use in adults and children. However, it's advisable to consult a healthcare professional before administering neem-based products to infants or very young children."
        )

        st.header("Gender Restrictions:")
        st.write("There are no specific gender restrictions for the use of neem. Both males and females can benefit from its medicinal properties.")

        st.header("Pregnancy Use Restriction:")
        st.write(
            "Pregnant women should exercise caution when using neem products, especially internally. High doses of neem may have contraceptive effects and could potentially lead to miscarriage. It's recommended that pregnant women consult a healthcare provider before using neem products during pregnancy."
        )

        st.header("Mode of Uses and Doses per Day:")
        st.write(
            "- Topical Application: Neem oil can be applied directly to the skin to treat various skin conditions. It should be diluted with a carrier oil (such as coconut or olive oil) to avoid irritation. Apply to affected areas as needed."
        )
        st.write(
            "- Oral Consumption: Neem supplements in the form of capsules or tablets are available for oral consumption. The recommended dosage varies depending on the specific product and the individual's health condition. It's essential to follow the instructions provided by the manufacturer or consult a healthcare professional for guidance."
        )
        st.write(
            "- Dental Care: Neem twigs or neem-based toothpaste can be used for oral hygiene. Chewing neem twigs or brushing with neem toothpaste helps to maintain dental health and prevent oral infections."
        )
        st.write(
            "- External Applications: Neem leaves can be boiled to make a decoction, which can then be used as a wash for wounds, or as a rinse for hair to combat dandruff and lice."
        )
        st.write(
            "- Insect Repellent: Neem oil can be diluted and sprayed on the skin or clothing to repel insects."
        )

        st.write(
            "Always ensure that you use neem products according to recommended guidelines and consult with a healthcare professional if you have any concerns or questions regarding its use or dosage."
        )

if __name__ == "__main__":
    main()
