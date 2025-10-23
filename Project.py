import streamlit as st
import pandas as pd
from collections import Counter
from streamlit_option_menu import option_menu
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")

#uploading files
express_gbp = 'Cleaned.csv'
df =  pd.read_csv('Cleaned.csv')
    
st.set_page_config(page_title='AI Usage')
st.title('AI USAGE BY STUDENTS :streamlit:')

#sidebar
with st.sidebar:
    selected = option_menu("Main Menu", options=['Home'], menu_icon='cast', icons=['house'], orientation='horizontal')
    st.write('## Filter Data')
    state = st.sidebar.multiselect('Select Region',options=df["State"].unique(),default=df['State'].unique())
    stream = st.sidebar.multiselect('Select Stream',options=df["Stream"].unique(),default=df['Stream'].unique())
    fdf = df[(df['State'].isin(state)) & (df['Stream'].isin(stream))]

#database
with st.expander('Database'):
        sel=st.multiselect('Filter',fdf.columns,default=df.columns)
        st.write(fdf[sel])

#columns
col1,col2,col3,col4=st.columns(4)
with col1:
     total_stu=fdf['Student_Name'].count()
     st.metric('Total Students👨‍🎓',f'{total_stu}')
with col2:
     usage_hrs=fdf['Daily_Usage_Hours'].sum()
     st.metric('Total Usage Hours Daily📈',f'{usage_hrs:.2f} Hrs')
with col3:
     avg_hrs=fdf['Daily_Usage_Hours'].mean()
     st.metric('Average Usage Hours Daily📉',f'{avg_hrs:.2f} Hrs')
with col4:
     trust=fdf['Trust_in_AI_Tools'].mean()
     st.metric('Trust in AI Tools💡',f'{trust:.2f}/5')

#graphs
tab1,tab2,tab3,tab4=st.tabs(['Map🌅','By Streams📊','By Year Of Study👨‍🎓','Use Cases📖'])
with tab1:
     fig7=px.choropleth(fdf,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",featureidkey='properties.ST_NM',locations='State',color='Daily_Usage_Hours',color_continuous_scale='Reds',height=800)
     fig7.update_geos(fitbounds="locations", visible=False)
     st.plotly_chart(fig7)
with tab2:
     fig3=px.box(fdf,x='Stream',y='Impact_on_Grades',color='Preferred_AI_Tool',title='Impact on Grades')
     st.plotly_chart(fig3)
     fig1=px.bar(fdf,x='Stream',y='Daily_Usage_Hours',color='Stream',title='Daily Usage Hrs of Students')
     st.plotly_chart(fig1)
     fig2=px.bar(fdf,x='Stream',y='Awareness_Level',color='Stream',title='Awareness_Level of Students')
     st.plotly_chart(fig2)
     
with tab3: 
     fig5=px.box(fdf,x='Year_of_Study',y='Impact_on_Grades',color='Year_of_Study',title='Impact on grades of Students')
     st.plotly_chart(fig5)
     fig_1=px.bar(fdf,x='Year_of_Study',y='Daily_Usage_Hours',color='Year_of_Study',title='Daily Usage Hrs of Students')
     st.plotly_chart(fig_1)
     fig8=px.pie(fdf,names='Year_of_Study',hole=0.4,title='Most Used in which Year')
     st.plotly_chart(fig8)

with tab4:
     fig_=px.pie(fdf,names='Do_Professors_Allow_Use',hole=0.4,title='Do Professors Allow Use Of AI')
     st.plotly_chart(fig_) 
     fig_2=px.pie(fdf,names='Internet_Access',hole=0.4,title='Internet Access of Students')
     st.plotly_chart(fig_2)
     fig_4=px.pie(fdf,names='Device_Used',hole=0.4,title='Device used by Students')
     st.plotly_chart(fig_4)
     fig_5=px.pie(fdf,names='Preferred_AI_Tool',hole=0.4,title='AI Tool used by Students')
     st.plotly_chart(fig_5)
     fig_6=px.pie(fdf,names='Willing_to_Pay_for_Access',hole=0.4,title='Students Willing to Pay for Access')

     st.plotly_chart(fig_6)










