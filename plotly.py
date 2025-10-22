import plotly_express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Sales Dashboard')
st.title('Sales Dashboard')

df=pd.read_csv('Online Sales Data.csv')
st.write(df)

st.sidebar.header('Filter data🔍')
region_filter=st.sidebar.multiselect('select regions',options=df['Region'].unique())
product_filter=st.sidebar.multiselect('select product',options=df['Product Category'].unique())
filtered_df=df[(df['Region'].isin(region_filter))&(df['Product Category'].isin(product_filter))]

col1,col2,col3=st.columns(3)
with col1:
    total_sales=filtered_df['Total Revenue'].sum()
    st.metric('Total Revenue',f'${total_sales:.2f}')
with col2:
    avg_sales=filtered_df['Total Revenue'].mean()
    st.metric('Avg Sales',f'${avg_sales:.2f}')
with col3:
    total_product=filtered_df['Product Name'].nunique()
    st.metric('Total Products',f'{total_product}')
    
tab1,tab2,tab3=st.tabs(["Sales by product📊","Sales by Region📶",'Temporal trends📉'])
with tab1:
    st.subheader('Sales by product')
    fig1=px.bar(filtered_df,x='Product Category',y='Total Revenue',color='Product Category')
    st.plotly_chart(fig1)

    st.subheader("order quantity(histogram)")
    fig6=px.histogram(filtered_df,x='Unit Price',nbins=5,color='Product Category', title="Distribution of order quantity")
    st.plotly_chart(fig6)

with tab2:
    st.subheader('Sales by Product Category')
    fig2=px.pie(filtered_df,names='Product Category', values='Total Revenue',title='Sales by Product Category')
    st.plotly_chart(fig2) 
    st.subheader('Sales by region')
    fig=px.pie(filtered_df,names='Region', values='Total Revenue',title='Sales by region')
    st.plotly_chart(fig)

    st.subheader('Revenue vs Quality (scatter plot)')
    fig3= px.scatter(filtered_df,x='Unit Price',y="Total Revenue", color='Product Category',size='Unit Price',hover_data=['Region'],title="Total Revenue vs order Quantity")
    st.plotly_chart(fig3)

    st.subheader("Revenue Distribution by product category(box plot)")
    fig4=px.box(filtered_df,x='Product Category',y='Total Revenue', color='Product Category',title='Revenue Distribution by product category')
    st.plotly_chart(fig4)

with tab3:
    st.subheader("Total Revenue over time")
    fig5=px.line(filtered_df,x='Date',y='Total Revenue',title="Revenue trends over time")
    st.plotly_chart(fig5)

    st.subheader("area chart")
    fig7 = px.area(filtered_df, x='Date', y='Total Revenue', title='Revenue Area Chart Over Time')
    st.plotly_chart(fig7, use_container_width=True)

    st.subheader("Total Revenue over time")
    fig5=px.line_3d(filtered_df,x='Date',y='Unit Price',z='Total Revenue',title="Revenue trends over time")
    st.plotly_chart(fig5)