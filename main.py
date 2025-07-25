import streamlit as st
from graph import build_graph
from chat_memory import conversation
from langchain.callbacks import LangChainTracer
from langchain.chains import ConversationChain



tracer = LangChainTracer()

st.set_page_config(page_title="🛒 Shopping Assistant")

st.title(" Помощник покупок")

user_input = st.text_input("Какая ваша цель для покупок?")
budget = st.number_input("Укажите ваш бюджет ($)", min_value=0.0, value=25.0, step=1.0)

if st.button("Создать список"):
    if not user_input.strip():
        st.warning("Пожалуйста, введите цель для покупок.")
    else:
        graph = build_graph()
        state = {
            "user_input": user_input,
            "budget": budget
        }

        with st.spinner("🤖 Обрабатываем..."):
            output = graph.invoke(state, callbacks=[tracer])

        if output.get("status") == "over_budget":
            st.error("❌ Бюджет превышен!")
            st.write(output.get("message"))
        else:
            st.success("✅ Список покупок готов!")
            st.subheader(f"📋 {output.get('recipe_name', 'Рецепт')}")
            
            products = output.get("shopping_list", [])
            total = output.get("total_cost", 0.0)

            for item in products:
                st.write(f"- {item['product']} — ${item['price']:.2f}")

            st.markdown(f"**💰 Общая стоимость:** ${total:.2f}")



